#include <stddef.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half = NULL;
	listint_t *prev_slow = *head;
	listint_t *mid_node = NULL;
	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		/* Find the middle and end of the first half */
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		/* Determine the middle node for odd length lists */
		if (fast != NULL)
		{
			mid_node = slow;
			slow = slow->next;
		}

		/* Reverse the second half and compare with the first half */
		second_half = slow;
		prev_slow->next = NULL;
		second_half = reverse_list(second_half);
		listint_t *p1 = *head;
		listint_t *p2 = second_half;

		while (p1 != NULL && p2 != NULL)
		{
			if (p1->n != p2->n)
			{
				is_palindrome = 0;
				break;
			}

			p1 = p1->next;
			p2 = p2->next;
		}

		/* Restore the original list by reversing the second half again */
		second_half = reverse_list(second_half);

		if (mid_node != NULL)
		{
			prev_slow->next = mid_node;
			mid_node->next = second_half;
		}
		else
		{
			prev_slow->next = second_half;
		}
	}

	return is_palindrome;
}
